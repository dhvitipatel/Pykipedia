import wx
import wikipedia
import wolframalpha
import speech_recognition as sr

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 250),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Pykipedia")
      
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hi! I am Pykipedia,  the Python Virtual Assistant. How can I help you?")
        my_sizer.Add(lbl, 3, wx.ALL, 25)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,100)) #white type box
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 3, wx.ALL, 20)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        if input == ' ':
            r = sr.Recognizer()
            mic = sr.Microphone()
            with mic as source:
                audio = r.listen(source)
            try:
                self.txt.SetValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print "Google Speech Recognition could not understand audio"
            except sr.RequestError as e:
                print "Could not request results from Google Speech Recognition service; {0}".format(e)
        else:
            try:
                #wolframalpha
                app_id = "XR9UWP-4X6GQ64VGL"
                client = wolframalpha.Client(app_id)
                res = client.query(input)
                answer = next(res.results).text
                print answer
            except:
                #wikipedia
                input = input.split(' ')
                input = " ".join(input[2: ])
                print wikipedia.summary(input)


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()





