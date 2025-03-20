**Background Project**

Dalam menghadapi era digitalisasi, bisnis perlu terus berinovasi agar tetap relevan dan kompetitif. Salah satu inovasi yang penting dalam bisnis ritel adalah penerapan sistem kasir otomatis untuk meningkatkan efisiensi transaksi dan memberikan pengalaman belanja yang lebih praktis bagi pelanggan.

**Requirements / Objectives**

*Sistem ini dikembangkan untuk memenuhi kebutuhan berikut:*

1.  Menyediakan fitur untuk menambahkan barang ke keranjang belanja.
2.  Memungkinkan pengguna memperbarui nama, jumlah, dan harga barang.
3.  Menghapus barang tertentu atau mengosongkan seluruh keranjang.
4.  Menghitung total harga dengan penerapan diskon otomatis.
5.  Menampilkan isi keranjang dalam bentuk tabel.


**Alur Code / Flowchart**

1.  Pengguna menambahkan item ke dalam keranjang belanja.
2.  Jika diperlukan, pengguna dapat memperbarui nama, jumlah, atau harga barang.
3.  Pengguna juga dapat menghapus barang tertentu atau menghapus semua barang dalam keranjang.
4.  Sistem memvalidasi input untuk memastikan tidak ada kesalahan dalam pesanan.
5.  Ketika pengguna ingin melihat ringkasan transaksi, sistem akan menampilkan daftar 
  barang dalam bentuk tabel.
6.  Sistem menghitung total harga, termasuk diskon jika memenuhi syarat.
7.  Hasil transaksi ditampilkan kepada pengguna.


**Penjelasan Functions dan Attributes**

*Attributes*:

1.  transaction_id: ID unik untuk transaksi.

2.  items: List yang menyimpan daftar barang dalam keranjang.

3.  counter: Counter otomatis untuk ID setiap item.

*Functions*:

1.  *add_item(item_name, quantity, price, category)*: Menambahkan barang ke dalam keranjang.

2.  *update_item_name(old_name, new_name)*: Memperbarui nama barang dalam keranjang.

3.  *update_item_qty(old_name, new_qty)*: Memperbarui jumlah barang.

4.  *update_item_price(old_name, new_price)*: Memperbarui harga barang.

5.  *delete_item(remove_item)*: Menghapus barang dari keranjang.

6.  *reset_transaction()*: Mengosongkan seluruh isi keranjang.

7.  *check_order()*: Memvalidasi apakah semua data dalam pesanan benar.

8.  *total_price()*: Menghitung total harga dengan diskon.

9.  *show_cart()*: Menampilkan isi keranjang dalam bentuk tabel.



**Demonstrasi Code dengan Test Case**

(project_supermarket/supermarket_project.png)



**Conclusion**

Sistem ini memberikan solusi  dalam mengelola transaksi belanja. Dengan fitur-fitur yang tersedia, pengguna dapat dengan mudah menambah, memperbarui, atau menghapus item dalam keranjang serta mendapatkan total harga dengan diskon otomatis.
