import requests


class GradientHandler:

    @staticmethod
    def download_gradient(w, h):
        url = f'https://picsum.photos/{w}/{h}'
        response = requests.get(url)
        filepath = f'gradients/background{w}x{h}.jpg'
        with open(filepath, 'wb') as f:
            for chunk in response:
                f.write(chunk)
        return filepath