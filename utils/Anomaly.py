from luminol.anomaly_detector import AnomalyDetector
import time

# 异常检测
class Anomaly:

    def __init__(self):
        pass

    def detect(self, ts):
        my_detector = AnomalyDetector(ts)
        score = my_detector.get_all_scores()
        anom_score = [] #给流量的异常度打个分

        for (timestamp, value) in score.iteritems():
            t_str = time.strftime('%d-%b-%Y %H:%M:%S', time.localtime(timestamp))
            anom_score.append([t_str, value])
        overall_stats = {} #整体的统计

        for score in anom_score:
            overall_stats[score[0]] = score[1]
        return overall_stats