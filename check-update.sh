#!/bin/sh
curl http://gwyddion.net/ 2>/dev/null | grep "Gwyddion:" |sed -ne 's,</a.*,,;s,.*>,,p'

