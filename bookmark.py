
import re
import traceback
from pathlib import Path
from typing import List
import fitz
from loguru import logger
from typing import List, Dict

def title_preprocess(line: str,page_number:int,offset:int,rules: List[Dict[str, str]] = None):
    pno = 1
    title = line
    # 把最右侧的数字当作页码，如果解析的数字超过pdf总页数，就从左边依次删直到小于pdf总页数为止
    m = re.search("(\d+)(?=\s*$)", line)
    if m is not None:
        pno = int(m.group(1))
        while pno + offset > page_number:
            pno = int(str(pno)[1:])
        title = line[:m.span()[0]]
    pno = pno + offset
    if not title.strip():  # 标题为空跳过
        return
    """提取标题层级和标题内容"""
    if rules is None:
        rules = [
            {"regex": "\s*(?:.*?)(\d+\.\d+\.\d+\.\d+)\s*(.*)", "level": 4},
            {"regex": "\s*(?:.*?)(\d+\.\d+\.\d+)\s*(.*)", "level": 3},
            {"regex": "\s*(?:.*?)(\d+\.\d+)\s*(.*)", "level": 2},
            {"regex": "\s*(?:.*)(第.+章)\s*(.*)", "level": 1},
            {"regex": "\s*(?:.*)(第.+节)\s*(.*)", "level": 2},
            {"regex": "\s*(?:.*)((Chapter) \d+\.?)\s*(.*)", "level": 1},
            {"regex": "\s*(?:.*)((Lesson) \d+\.?)\s*(.*)", "level": 2},
            {"regex": "\s*(?:.*)([一二三四五六七八九十]+[、.])\s*(.*)", "level": 1},
        ]

    title = title.rstrip()
    title = title.replace(" ", "")
    for rule in rules:
        try:
            m = re.match(rule["regex"], title)
            if m is not None:
                return {
                    'text': f"{m.group(1)} {m.group(2)}",
                    'level': rule["level"](m) if callable(rule["level"]) else rule["level"],
                    'pno':pno
                }

        except re.error as e:
            print(f"Invalid regex: {rule['regex']}. Error: {e}")
    # 默认返回值
    return {'text': title, 'level': 1,'pno':pno}


def add_toc_from_file(toc_path: str, doc_path: str, offset: int, output_path= './result/out/'):
    dic_path = './result/txt/dic.txt'
    try:
        doc: fitz.Document = fitz.open(doc_path)
        p = Path(doc_path)
        toc_path = Path(toc_path)
        toc = []
        page_number=doc.page_count
        if toc_path.suffix == ".txt":
            with open(toc_path, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip(): # 标题为空跳过
                        continue
                    if title_preprocess(line,page_number,offset)!=None:
                        res = title_preprocess(line,page_number,offset)
                        print(res)
                        level, title ,pno= res['level'], res['text'],res['pno']
                        toc.append([level, title, pno, {"kind":1, "zoom":1, "to": fitz.Point(0, 0)}])
                        # [level, title, page [, dest]]

        # 校正层级
        levels = [v[0] for v in toc]
        diff = [levels[i+1]-levels[i] for i in range(len(levels)-1)]
        indices = [i for i in range(len(diff)) if diff[i] > 1]
        #确保
        if toc[0][0]!=1:
            toc.insert(0,[1,toc[0][1],offset+1,{"kind":1, "zoom":1, "to": fitz.Point(0, 0)}])
            for idx in indices:
                toc[idx][0] = toc[idx+1][0]
        for i in range(len(toc)-1):
            if toc[i+1][0]==toc[i][0] or toc[i+1][0]==toc[i][0]+1 or toc[i+1][0]<toc[i][0]:
                continue
            else :
                toc[i+1][0]=toc[i][0]+1

        #return toc
        logger.debug(toc)
        doc.set_toc(toc)
        if output_path is None:
            output_path = str(p.parent / f"{p.stem}-加书签目录.pdf")
        if output_path != doc_path:
            doc.save(output_path+f"{p.stem}-加书签目录.pdf", garbage=3, deflate=True)
        else:
            doc.save(doc_path, deflate=True, incremental=True)

    except:
        logger.error(traceback.format_exc())

if __name__ == "__main__":

    pdf_path=r'C:\Code\计算机视觉教程.pdf'
    file_path = './result/txt/dic.txt'
    offset=10
    out_path='./result/out/'
    c=add_toc_from_file(file_path,pdf_path,offset,out_path)
