import  logging
class Logs01:
    def logs(self):
        logging.basicConfig(filename="C:\\Users\\91789\\PycharmProjects\\flair\\testCases\\Reports\\logfile.log",
                            filemode="w",
                            format="%(asctime)s - %(levelname)s -%(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")
        log=logging.getLogger()
        log.setLevel(logging.INFO)
        return log