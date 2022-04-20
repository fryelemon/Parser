import requests
from bs4 import BeautifulSoup

main_url = 'https://www.ozon.ru/product/drazhe-tic-tac-' \
           'so-vkusom-apelsina-16-g-138860274/?advert=iQe1' \
           'PJp0D_uGD7xEp_jYNdFgeDufu1wiDeCpVoqeNriLLyEJQDA4-' \
           'qsPgK-Su1uymiR7W9ovxW1lssyLA_vbZNRUZ2Gvlt26VkWV58' \
           'h7ZnERkxuVd26KZPPG52Y7Ng6FLFEpXOMOu2MLh5__bu7LXIj' \
           'qJWaywbOw8kCdASCKN_0W-PM6UVFHGRqilXfcnpaw7JuNGp7' \
           'gCW9Ka2g8AgnUxitHiUqpHPmzUJ3mIZiomuYre8Nq6B6ahCcIKtMhrIRS0MfmHSPQfDmIkZrnEiz1tXKlZLtJmOGgWDXE85Uo-JDbFoaotbPhrso5x-Yvf5_d4MlzETmLnG5s-4HlKEYuB2Or_s4dsdLhJqS4CF6eNezCuodkYPKlfEIg1GN8JR2iKnd0Qx98Z7F8i1xvymwiHU1Cc6wEd2IcG7eJWZHUi_kbI5kh-Nk4gKxGXoFLpMWRZF0xFpsocGZg1cnCWPiyeV_ElMmBweHbrxxMcEclXBi22JjRJ2qSNzoapA0jhOcf3gx4RJFRRYl7eqxaOM2NbLCJpridVGLzx9stWnzCKMQ&sh=n5jy89pt1g'
page = requests.get(main_url)

soup = BeautifulSoup(page.text, "html.parser")
print(soup.findAll('body'))
