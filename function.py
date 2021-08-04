import rumps
import webbrowser
import time

@rumps.clicked("Scan")
def about(sender):
    webbrowser.open('https://github.com/jaiveertalwar/Virusr/wiki/You-fell-for-it!')
    time.sleep(5)


@rumps.clicked("Update")
def about(sender):
    webbrowser.open('https://github.com/jaiveertalwar/Virusr/wiki/You-fell-for-it!')
    time.sleep(5)


@rumps.clicked("Remove Threats")
def about(sender):
    webbrowser.open('https://github.com/jaiveertalwar/Virusr/wiki/You-fell-for-it!')
    time.sleep(5)

app = rumps.App("MvAB", title='AV')
app.menu = [
    rumps.MenuItem('SAnti Virus'),
    'By SAV Team',
]
app.run()
