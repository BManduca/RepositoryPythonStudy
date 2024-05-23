from barcode import Code128
from barcode.writer import ImageWriter

# gerenciador para a biblioteca do barcode
class BarcodeHandler:
    
    def create_barcode(self, product_code:str) -> str:
        generate_tag = Code128(product_code, writer=ImageWriter())
    
        path_from_tag = f'./Public/BarCodeGenerate/{generate_tag}'
        generate_tag.save(path_from_tag)
        
        return path_from_tag
    