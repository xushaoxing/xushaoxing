import unittest
from Common.config_manage import ConfigManager
from testcase01.reg_test import Reg
from BeautifulReport import BeautifulReport as bf
# from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # suite.addTest(Reg().test_reg_01())
    suite.addTest(loader.loadTestsFromTestCase(Reg))
    run = bf(suite)
    run.report(filename=ConfigManager().REPORT_NAME, description='测试', report_dir=ConfigManager().REPORT_FILE)



    '''
    多线程执行
    from unittestreport import TestRunner
    # 加载套件
    suite = unittest.defaultTestLoader.discover(CASE_DIR)
    # 执行用例
    runner = TestRunner(suite,
                        filename=conf.get('report', "filename"),
                        report_dir=REPORT_DIR,
                        title='测试报告',
                        tester='木森',
                        desc="木森执行测试生产的报告",
                        templates=1
                        )
    # 指定三个线程运行测试用例
    runner.run(thread_count=3)
    '''


