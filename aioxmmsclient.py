"""asyncio (PEP 3156) connector for the XMMS2 Python bindings."""


class AIOXMMSConnector:
    def __init__(self, loop, xmms):
        self.loop = loop
        self.xmms = xmms
        self.has_writer = False
        self.connect()

    def handle_out(self):
        if self.xmms.want_ioout():
            self.xmms.ioout()

        if not self.xmms.want_ioout() and self.has_writer:
            self.loop.remove_writer(self.xmms.get_fd())
            self.has_writer = False

    def need_out(self, i):
        if self.xmms.want_ioout() and not self.has_writer:
            self.loop.add_writer(self.xmms.get_fd(), self.handle_out)
            self.has_writer = True

    def connect(self):
        self.xmms.set_need_out_fun(self.need_out)
        self.loop.add_reader(self.xmms.get_fd(), self.xmms.ioin)


def add_xmms_to_event_loop(loop, xmms):
    """Tells the loop to handle the XMMS2 connection's I/O."""
    return AIOXMMSConnector(loop, xmms)


def remove_xmms_from_event_loop(loop, xmms):
    """Stops handling the XMMS2 connection's I/O."""
    loop.remove_reader(xmms.get_fd())
    loop.remove_writer(xmms.get_fd())
