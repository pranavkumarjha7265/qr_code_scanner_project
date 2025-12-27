import qrcode
# take upi id as input
upi_id=input("Enter the upi id: ")
Recipient=input("enter name: ")
# upi://pay ? pa=upi_id & pn=NAME & am=amount & cu=current & tn=message
# defining payment url based on upi_id and payment app
phonepay_url=f'upi://pay?pa-{upi_id}&pn={Recipient.replace("","%20")}&cu=INR'
paytm_url=f'upi://pay?pa-{upi_id}&pn={Recipient.replace("","%20")}&cu=INR'
google_pay_url=f'upi://pay?pa-{upi_id}&pn={Recipient.replace("","%20")}&cu=INR'
# create qr codes for each payment app

phonepay_qr=qrcode.make(phonepay_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

# save the qr to image file
phonepay_qr.save('phonepay_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')


# dispay qr code 
from PIL import Image 
phonepay_qr.show()
paytm_qr.show()
google_pay_qr.show()






#7050040030@ptyes