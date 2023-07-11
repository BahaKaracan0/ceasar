# ceasar
# Caesar Encryption and Decryption

This is a Python program that provides a graphical user interface (GUI) for encrypting and decrypting text using the Caesar cipher algorithm.

The program uses the `tkinter` library to create the GUI. It allows the user to enter the text to be encrypted or decrypted, as well as the key (shift) value for the cipher. The text is then processed based on the selected operation (encrypt or decrypt).

The `CaesarEncryption` class represents the main application window. It initializes the GUI components, such as labels, input fields, buttons, and text areas, using the `tkinter` library. The `encrypt` and `decrypt` methods are responsible for handling the button click events and performing the respective operations.

The `caesar_encrypt` method takes a text and a key as input and performs the encryption using the Caesar cipher algorithm. It iterates over each character in the text and shifts it by the specified key value. The encrypted text is then returned.

The `caesar_decrypt` method takes an encrypted text and a key as input and performs the decryption using the Caesar cipher algorithm. It reverses the encryption process by shifting each character back by the specified key value. The decrypted text is then returned.

To run the program, create an instance of the `CaesarEncryption` class and call the `mainloop` method on the root window. This will start the GUI application and allow you to interact with it.

You can customize the GUI appearance and functionality as per your requirements. Feel free to modify the code and experiment with different features.

---------------------------------------------------------------------------------------------------------------------------------------
# Sezar Şifreleme ve Şifre Çözme

Bu, Sezar şifreleme algoritmasını kullanarak metinlerin şifrelenmesini ve şifrelenmiş metinlerin çözülmesini sağlayan bir Python programıdır.

Program, kullanıcıya Sezar şifrelemesi için bir grafiksel kullanıcı arayüzü (GUI) sunar. Kullanıcı, şifrelenmek veya çözülmek istenen metni ve şifreleme anahtarını girebilir. Ardından, seçilen işleme (şifrele veya çöz) göre metin işlenir.

`tkinter` kütüphanesini kullanarak GUI bileşenleri oluşturur. Etiketler, giriş alanları, düğmeler ve metin alanları gibi GUI bileşenleri oluşturulur.

`CaesarEncryption` sınıfı, ana uygulama penceresini temsil eder. `tkinter` kütüphanesini kullanarak etiketler, giriş alanları, düğmeler ve metin alanları gibi GUI bileşenlerini başlatır. `encrypt` ve `decrypt` yöntemleri, düğme tıklama olaylarını işlemek ve ilgili işlemleri gerçekleştirmekten sorumludur.

`caesar_encrypt` yöntemi, bir metin ve bir anahtar alır ve Sezar şifreleme algoritmasını kullanarak şifrelemeyi gerçekleştirir. Metindeki her karakteri belirtilen anahtar değeri kadar kaydırır. Şifrelenmiş metin döndürülür.

`caesar_decrypt` yöntemi, bir şifrelenmiş metin ve bir anahtar alır ve Sezar şifreleme algoritmasını kullanarak şifre çözme işlemini gerçekleştirir. Her karakteri belirtilen anahtar değeri kadar geri kaydırarak şifreleme işlemini tersine çevirir. Çözülmüş metin döndürülür.

Programı çalıştırmak için, `CaesarEncryption` sınıfından bir örnek oluşturun ve kök pencere üzerinde `mainloop` yöntemini çağırın. Bu, GUI uygulamasını başlatacak ve kullanıcıyla etkileşime geçmenizi sağlayacaktır.

GUI'nin görünümünü ve işlevselliğini ihtiyaçlarınıza göre özelleştirebilirsiniz. Kodu değiştirerek ve farklı özelliklerle deney yaparak kendinize özgü hale getirebilirsiniz.

