# Copyright 2022 Tiernan8r
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from PySide6 import QtWidgets
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar

matplotlib.use('Qt5Agg')


class EmbeddedGraph(QtWidgets.QWidget):

    def __init__(self, graph_widget: QtWidgets.QWidget):
        super().__init__(parent=graph_widget)
        self.graph_widget = graph_widget

        self._setup_canvas()
        self._setup_layouts()

    def hide(self) -> None:
        super().hide()
        self.graph_widget.hide()
        self.figure_canvas.hide()
        self.toolbar.hide()

    def show(self) -> None:
        super().show()
        self.graph_widget.show()
        self.figure_canvas.show()
        self.toolbar.show()

    def _setup_canvas(self):
        self.figure = Figure()
        self.figure.tight_layout()
        self.axes = self.figure.add_subplot()

        self.figure_canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.figure_canvas, self)

    def _setup_layouts(self):
        graph_frame_layout = QtWidgets.QGridLayout(parent=self.graph_widget)
        graph_frame_layout.addWidget(self.toolbar)
        graph_frame_layout.addWidget(self.figure_canvas)

        self.setLayout(graph_frame_layout)

        parent_layout = QtWidgets.QHBoxLayout(parent=self.graph_widget)
        parent_layout.addWidget(self)

        self.graph_widget.setLayout(parent_layout)

        self.figure_canvas.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.figure_canvas.updateGeometry()

    def _plot_line(self, x, y, title, xlabel, ylabel, legend=None,
                   line_style="-"):
        self.axes.plot(x, y, line_style)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.set_title(title)
        if legend is not None:
            self.axes.legend(legend)