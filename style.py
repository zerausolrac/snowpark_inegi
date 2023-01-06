def divContainer():
    return f'''<style>[data-testid="metric-container"]''' + \
        "{border: 1px solid #D77777;"+ \
        "width: 250px;"+ \
        "border-radius: 15px;"+ \
        "margin: 0 auto;"+ \
        "text-items: center;"+ \
        "padding-left: 20px;"+ \
        "display: in-line;"+ \
        "}</style>"


def formatoNumero(num:int):
    return f'{num:,}'