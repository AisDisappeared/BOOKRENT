from datetime import datetime, timedelta 
import pyotp


def send_otp(request):
    # Time-Based One-Time Password 
    totp = pyotp.TOTP(pyotp.random_base32(),interval=60)
    # fetching the otp 
    otp = totp.now()
    # storing the otp secret key in sessions variables
    request.session['otp_secret_key'] = totp.secret
    # calculating the validation time 
    valid_date = datetime.now() + timedelta(minutes=1)
    # storing that in sessions 
    request.session['otp_valid_date'] = str(valid_date)

    print(otp)

