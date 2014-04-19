aioxmmsclient
=============

`asyncio <https://docs.python.org/3.4/library/asyncio.html>`_ connector for
the XMMS2 Python bindings.


Example usage
-------------

.. code-block:: python

    import asyncio

    import xmmsclient
    import aioxmmsclient


    xmms = xmmsclient.XMMS("xmms2-aio-test")
    xmms.connect()

    loop = asyncio.get_event_loop()
    aioxmmsclient.add_xmms_to_event_loop(loop, xmms)

    def current_id(result):
        print("current id", result.value())

    xmms.broadcast_playback_current_id(current_id)
    xmms.playback_current_id(current_id)

    loop.run_forever()
