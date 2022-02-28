import os
import subprocess
import sys

inputs = [
	'lib/internal/bootstrap_node.js',
	'lib/async_hooks.js',
	'lib/assert.js',
	'lib/buffer.js',
	'lib/child_process.js',
	'lib/console.js',
	'lib/constants.js',
	'lib/crypto.js',
	'lib/cluster.js',
	'lib/dgram.js',
	'lib/dns.js',
	'lib/domain.js',
	'lib/events.js',
	'lib/fs.js',
	'lib/http.js',
	'lib/http2.js',
	'lib/_http_agent.js',
	'lib/_http_client.js',
	'lib/_http_common.js',
	'lib/_http_incoming.js',
	'lib/_http_outgoing.js',
	'lib/_http_server.js',
	'lib/https.js',
	'lib/inspector.js',
	'lib/module.js',
	'lib/net.js',
	'lib/os.js',
	'lib/path.js',
	'lib/perf_hooks.js',
	'lib/process.js',
	'lib/punycode.js',
	'lib/querystring.js',
	'lib/readline.js',
	'lib/repl.js',
	'lib/stream.js',
	'lib/_stream_readable.js',
	'lib/_stream_writable.js',
	'lib/_stream_duplex.js',
	'lib/_stream_transform.js',
	'lib/_stream_passthrough.js',
	'lib/_stream_wrap.js',
	'lib/string_decoder.js',
	'lib/sys.js',
	'lib/timers.js',
	'lib/tls.js',
	'lib/_tls_common.js',
	'lib/_tls_legacy.js',
	'lib/_tls_wrap.js',
	'lib/tty.js',
	'lib/url.js',
	'lib/util.js',
	'lib/v8.js',
	'lib/vm.js',
	'lib/zlib.js',
	'lib/internal/async_hooks.js',
	'lib/internal/buffer.js',
	'lib/internal/child_process.js',
	'lib/internal/cluster/child.js',
	'lib/internal/cluster/master.js',
	'lib/internal/cluster/round_robin_handle.js',
	'lib/internal/cluster/shared_handle.js',
	'lib/internal/cluster/utils.js',
	'lib/internal/cluster/worker.js',
	'lib/internal/encoding.js',
	'lib/internal/errors.js',
	'lib/internal/freelist.js',
	'lib/internal/fs.js',
	'lib/internal/http.js',
	'lib/internal/inspector_async_hook.js',
	'lib/internal/linkedlist.js',
	'lib/internal/loader/Loader.js',
	'lib/internal/loader/ModuleMap.js',
	'lib/internal/loader/ModuleJob.js',
	'lib/internal/loader/ModuleWrap.js',
	'lib/internal/loader/ModuleRequest.js',
	'lib/internal/loader/search.js',
	'lib/internal/safe_globals.js',
	'lib/internal/net.js',
	'lib/internal/module.js',
	'lib/internal/os.js',
	'lib/internal/process/next_tick.js',
	'lib/internal/process/promises.js',
	'lib/internal/process/stdio.js',
	'lib/internal/process/warning.js',
	'lib/internal/process.js',
	'lib/internal/querystring.js',
	'lib/internal/process/write-coverage.js',
	'lib/internal/readline.js',
	'lib/internal/repl.js',
	'lib/internal/socket_list.js',
	'lib/internal/test/unicode.js',
	'lib/internal/trace_events_async_hooks.js',
	'lib/internal/url.js',
	'lib/internal/util.js',
	'lib/internal/util/types.js',
	'lib/internal/http2/core.js',
	'lib/internal/http2/compat.js',
	'lib/internal/http2/util.js',
	'lib/internal/v8_prof_polyfill.js',
	'lib/internal/v8_prof_processor.js',
	'lib/internal/streams/lazy_transform.js',
	'lib/internal/streams/BufferList.js',
	'lib/internal/streams/legacy.js',
	'lib/internal/streams/destroy.js',
	'lib/internal/wrap_js_stream.js',
	'deps/v8/tools/splaytree.js',
	'deps/v8/tools/codemap.js',
	'deps/v8/tools/consarray.js',
	'deps/v8/tools/csvparser.js',
	'deps/v8/tools/profile.js',
	'deps/v8/tools/profile_view.js',
	'deps/v8/tools/logreader.js',
	'deps/v8/tools/tickprocessor.js',
	'deps/v8/tools/SourceMap.js',
	'deps/v8/tools/tickprocessor-driver.js',
	'deps/node-inspect/lib/_inspect.js',
	'deps/node-inspect/lib/internal/inspect_client.js',
	'deps/node-inspect/lib/internal/inspect_repl.js',
	'lib/_third_party_main.js',
	'./config.gypi',
	'src/notrace_macros.py',
	'src/nolttng_macros.py',
	'src/noperfctr_macros.py',
]

noderoot = sys.argv[1]

mtimes = [
    os.path.getmtime(os.path.join(noderoot, inFile)) for inFile in inputs
]

mtimes += [ os.path.getmtime(sys.argv[0]) ]

mtimes.sort()
mtimes.reverse()

outFile = os.path.join(noderoot, 'src/node_javascript.cc')

if not os.path.exists(outFile) or os.path.getmtime(outFile) < mtimes[0]:
	subprocess.check_call(['python', 'tools/js2c.py', 'src/node_javascript.cc'] + inputs, cwd = noderoot)
