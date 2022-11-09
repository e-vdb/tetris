"""
Provides a simple stopwatch class for tkinter gui.

Source: https://code.activestate.com/recipes/124894-stopwatch-in-tkinter/

"""
import time
import tkinter as tk


class StopWatch(tk.Frame):
    """Implement a stop watch frame widget."""

    def __init__(self, parent=None, **kw):
        """Initialize the class."""
        tk.Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = tk.StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        """Make the time label."""
        label = tk.Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        label.pack(fill=tk.X, expand=tk.NO, pady=2, padx=2)

    def _update(self):
        """Update the label with elapsed time."""
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        """Set the time string to Minutes:Seconds."""
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        self.timestr.set('%02d:%02d' % (minutes, seconds))

    def Start(self):
        """Start the stopwatch, ignore if running."""
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

    def Stop(self):
        """Stop the stopwatch, ignore if stopped."""
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

    def Reset(self):
        """Reset the stopwatch."""
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)
