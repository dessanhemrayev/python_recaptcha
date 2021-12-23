import requests
# def clean(self):
#         ca = self.request.POST["g-recaptcha-response"]
#         url = "https://www.google.com/recaptcha/api/siteverify"
#         params = {
#             'secret': config.RECAPTCHA_SECRET_KEY,
#             'response': ca,
#             'remoteip': utility.get_client_ip(self.request)
#         }
#         verify_rs = requests.get(url, params=params, verify=True)
#         verify_rs = verify_rs.json()
#         status = verify_rs.get("success", False)
#         if not status:
#             raise forms.ValidationError(
#                 _('Captcha Validation Failed.'),
#                 code='invalid',
#             )

# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

def clean():
        # ca = requests.post["g-recaptcha-response"]
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': '6LedBUIdAAAAAJHqPw3eftlXezax9iNaXryoWDpZ',
            'response': '03AGdBq26POLKGzK-stvOEn4kTN8Rd76Uj87HXtKb5A25xjotzDFQFOxVdrajAqcJ2-36Da1qbzGvNckOx6Stak-U_9Ku7K_9s7qOA5V_sQ5yFHy-6IUwi6jU-fyBTIVyGeZjfSdecU2BN5D4bK0YUFDlwlbRji6_lWVvMk9pyAXTJA_jhyNnL8rSGLoNuux99obPovv3Bn2-EiTqzzmnwuFMG-PnxFkVg1wdBH_lOS5bAL-6czYrc8MECmLcQQrzqG4yqbrOQq0hLJzOeKEEH9avdlYeBYTMdRg2be63gpZdycuP5MszDBXP2rCt6ON90V5opsNPlAn__1Nu1L-l14HZrSavLghljHcCQbIFnzZQyTvESjlh8gqvMJnurP-g2Qr6-Ys0D1SEwmyWaodgfDtKNYj9nQ1oDTbr3pqkt8GDm36cbPMZUd8yPHY-JYf_temcM-MciC3CE',
            'remoteip': '91.240.209.176'
        }
        verify_rs = requests.get(url, params=params, verify=True)
        verify_rs = verify_rs.json()
        status = verify_rs.get("success", False)
        print(status)
        if not status:
            print('invalid')
        else:
            print(status)


if __name__ == "__main__":
	clean()


import requests

url = "https://www.google.com/recaptcha/api/siteverify?secret=6LedBUIdAAAAAJHqPw3eftlXezax9iNaXryoWDpZ&response=03AGdBq26POLKGzK-stvOEn4kTN8Rd76Uj87HXtKb5A25xjotzDFQFOxVdrajAqcJ2-36Da1qbzGvNckOx6Stak-U_9Ku7K_9s7qOA5V_sQ5yFHy-6IUwi6jU-fyBTIVyGeZjfSdecU2BN5D4bK0YUFDlwlbRji6_lWVvMk9pyAXTJA_jhyNnL8rSGLoNuux99obPovv3Bn2-EiTqzzmnwuFMG-PnxFkVg1wdBH_lOS5bAL-6czYrc8MECmLcQQrzqG4yqbrOQq0hLJzOeKEEH9avdlYeBYTMdRg2be63gpZdycuP5MszDBXP2rCt6ON90V5opsNPlAn__1Nu1L-l14HZrSavLghljHcCQbIFnzZQyTvESjlh8gqvMJnurP-g2Qr6-Ys0D1SEwmyWaodgfDtKNYj9nQ1oDTbr3pqkt8GDm36cbPMZUd8yPHY-JYf_temcM-MciC3CE&remoteip=91.240.209.176"

payload={}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)