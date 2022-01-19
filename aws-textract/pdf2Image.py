from pdf2image import convert_from_path
import os

#filename
Root_dir = 'C:/Users/lenovo/PycharmProjects/aws-textract/Data/'

#conversion
def convert_pdf(pdf_path, save_dir, res=400):
    print(pdf_path)
    pages = convert_from_path(pdf_path,res)

    name_with_extension = pdf_path.rsplit('/')[-1]
    name = name_with_extension.rsplit('.')[0]

    out_path = os.path.join(save_dir,name)
    os.makedirs(out_path)

    for idx,page in enumerate(pages):
        page.save(f'{out_path}/{name}_{idx}.png','PNG')