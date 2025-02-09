import qrcode

# Tacking input from user
upi_id = input("Enter your UPI ID = ")

# upi://pay?pa={upi_id}&pn=NAME&am=Amount&cu=CURRENCY&tn=Message

# Defining the payment URL based on the UPI ID and the Payment app 
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Creating a QR code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Saving the QR codes as images
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# showing qr codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()