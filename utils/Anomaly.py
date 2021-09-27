from luminol.anomaly_detector import AnomalyDetector
import time

# �쳣���
class Anomaly:

    def __init__(self):
        pass

    def detect(self, ts):
        my_detector = AnomalyDetector(ts)
        score = my_detector.get_all_scores()
        anom_score = [] #���������쳣�ȴ����

        for (timestamp, value) in score.iteritems():
            t_str = time.strftime('%d-%b-%Y %H:%M:%S', time.localtime(timestamp))
            anom_score.append([t_str, value])
        overall_stats = {} #�����ͳ��

        for score in anom_score:
            overall_stats[score[0]] = score[1]
        return overall_stats