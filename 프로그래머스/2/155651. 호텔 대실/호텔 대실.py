from datetime import datetime, timedelta
def solution(book_time):
    answer=0
    ttime=[0]*(24*60+10)
    real_time=[]
    for i in range(len(book_time)):
        if datetime.strptime(book_time[i][1], '%H:%M')>=datetime.strptime('23:50', '%H:%M'):
            start_time_x = datetime.strptime(book_time[i][0], '%H:%M')
            end_time_x = datetime.strptime(book_time[i][1], '%H:%M')
            start_minutes = int(start_time_x.strftime('%H')) * 60 + int(start_time_x.strftime('%M'))
            end_minutes = int(end_time_x.strftime('%H')) * 60 + int(end_time_x.strftime('%M'))
            real_time.append([start_minutes, end_minutes])
        else:    
            start_time_x = datetime.strptime(book_time[i][0], '%H:%M')
            end_time_x = datetime.strptime(book_time[i][1], '%H:%M') + timedelta(minutes=10)
            start_minutes = int(start_time_x.strftime('%H')) * 60 + int(start_time_x.strftime('%M'))
            end_minutes = int(end_time_x.strftime('%H')) * 60 + int(end_time_x.strftime('%M'))
            real_time.append([start_minutes, end_minutes])
        for x in range(real_time[i][0],real_time[i][1]):
            ttime[x]+=1

    return max(ttime)