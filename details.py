from pam.pam import InApp, BaseApp

Whatbot = BaseApp('Whatbot', '00.10.01', 'Marketing', 'Chatbot', date="4/3/1445", application_nu=2)

Responder = InApp("Responder", "00.02.04", "13/3/1445", "Reply to messages automaticly", 1, 'Whatbot')


if __name__=="__main__":
    BaseApp.printApplication()
    BaseApp.printApps()
