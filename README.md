# flavim_image_processing

Description. 

| The package flavim_image_processing is used to: |
| ------------------------------------------------ |
| - processar imagens usando scikit-image         |

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flavim_image_processing

```bash
pip install flavim_image_processing
```

## Usage

```python
from flavim_image_processing.processing import combination
from flavim_image_processing.utils import io, plot

image1 = io.read_image("caminho_da_imagem")
image2 = io.read_image("caminho_da_imagem")

result_image = combination.transfer_histogram(image1, image2)

plot.plot_result(image1, image2, result_image)

```

## Author

Flavim by Karina Kato

## License

[MIT](https://choosealicense.com/licenses/mit/)
