ControlFocus("ѡ��Ҫ���ص��ļ�", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("ѡ��Ҫ���ص��ļ�", "", "Edit1", $CmdLine[1])
Sleep(2000)
ControlClick("ѡ��Ҫ���ص��ļ�", "","Button1");