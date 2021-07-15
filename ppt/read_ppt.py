from pptx import Presentation
prs = Presentation("测试.pptx")
for index, slide in enumerate(prs.slides):
    print(f"第 {index+1} 页")
    for shape in slide.shapes:
        if shape.has_text_frame:
            text_frame = shape.text_frame
            print(text_frame.text)