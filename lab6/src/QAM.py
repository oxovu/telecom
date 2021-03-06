#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Qam
# Generated: Wed May 22 11:29:14 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy
import sip
import sys
from gnuradio import qtgui


class QAM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Qam")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Qam")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "QAM")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.update_per = update_per = 0.5
        self.samp_rate = samp_rate = 320e3

        ##################################################
        # Blocks
        ##################################################
        self.digital_qam_mod_0 = digital.qam.qam_mod(
          constellation_points=16,
          mod_code="gray",
          differential=True,
          samples_per_symbol=2,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.c_qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.c_qtgui_time_sink_x_0.set_update_time(update_per)
        self.c_qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.c_qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.c_qtgui_time_sink_x_0.enable_tags(-1, True)
        self.c_qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.c_qtgui_time_sink_x_0.enable_autoscale(False)
        self.c_qtgui_time_sink_x_0.enable_grid(False)
        self.c_qtgui_time_sink_x_0.enable_axis_labels(True)
        self.c_qtgui_time_sink_x_0.enable_control_panel(False)
        self.c_qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.c_qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 3, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.c_qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.c_qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.c_qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.c_qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.c_qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.c_qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.c_qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._c_qtgui_time_sink_x_0_win = sip.wrapinstance(self.c_qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._c_qtgui_time_sink_x_0_win)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.b_qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.b_qtgui_waterfall_sink_x_0_0.set_update_time(update_per/4)
        self.b_qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.b_qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.b_qtgui_waterfall_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.b_qtgui_waterfall_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.b_qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.b_qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.b_qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.b_qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])

        self.b_qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, 10)

        self._b_qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.b_qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._b_qtgui_waterfall_sink_x_0_0_win)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, 10000000)), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.0025, 0)
        self.a_qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.a_qtgui_const_sink_x_0_0.set_update_time(update_per)
        self.a_qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.a_qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.a_qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.a_qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.a_qtgui_const_sink_x_0_0.enable_grid(False)
        self.a_qtgui_const_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.a_qtgui_const_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.a_qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.a_qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.a_qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.a_qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.a_qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.a_qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.a_qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._a_qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.a_qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._a_qtgui_const_sink_x_0_0_win)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_qam_mod_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.c_qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.a_qtgui_const_sink_x_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.b_qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.blocks_add_xx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "QAM")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_update_per(self):
        return self.update_per

    def set_update_per(self, update_per):
        self.update_per = update_per
        self.c_qtgui_time_sink_x_0.set_update_time(self.update_per)
        self.b_qtgui_waterfall_sink_x_0_0.set_update_time(self.update_per/4)
        self.a_qtgui_const_sink_x_0_0.set_update_time(self.update_per)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.c_qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.b_qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate)


def main(top_block_cls=QAM, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
