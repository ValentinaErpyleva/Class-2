class Application:
    print('Choose status Turn_off=1 Turn_on=2')
    status = (input())
    if status == '1':
        def status_off(self):
            print(status)
    elif status == "2":
        def status_on(self):
            print(status)

p=Application()
p.status_on('OK')
p.status_off('STOP')
class ActivityRecognize(Application):
    type="0"
    def __init__(self,status):
        super().__init__(status)
    def ActivityType_on(self):
        print('Recognize')
        p=ActivityRecognize('0')
        p.ActivityType_on()
    type='1'

    def ActivityType_off(self):
        print ('Stop')
        p=ActivityRecognize('1')
        p.ActivityType_off()
    dev=ActivityRecognize(Application)
    dev.ActivityRecognize_off

class PowerSwitch(Application):
    def __init__(self,status):
        super().__init__(status)
    def turn_off(self):
        print("PowerSwitch_off")














