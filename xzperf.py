# #!/usr/bin/python
#
# import os
# import sys
# import psutil
# import subprocess
# import time
# from multiprocessing import Pool
# import hashlib
# import matplotlib.pyplot as plt
# from space import Space
#
#
# def invoke_xz(chain):
#     suf = hashlib.md5(chain.encode("ascii")).hexdigest()
#     args = ["d:/my/src/xzperf/xz.exe",
#             "-z", "-k", "--format", "lzma", "-f", "-S", "." + suf,
#             chain, "z.tar"]
#     p = psutil.Popen(args, cwd="r:/", shell=False,
#                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     # print("%s: %s" % (p.pid, chain))
#     pp = psutil.Process(p.pid)
#     ct = pp.cpu_times()
#     t1 = time.time()
#     error = ""
#     while True:
#         try:
#             ct = pp.cpu_times()
#         except Exception:
#             pass
#         if time.time() - t1 > 300:
#             return (time.time() - t1, 0, chain)
#         p.poll()
#         if p.returncode is not None:
#             _, err = p.communicate()
#             error += err.decode("utf-8")
#             if p.returncode != 0:
#                 return (time.time() - t1, 0, chain, error)
#             sz = os.stat("r:/z.tar."+suf).st_size
#             os.remove("r:/z.tar."+suf)
#             return (ct.user, sz, chain, error)
#         time.sleep(0.01)
#
#
# def chaingen():
#     s = Space()
#     s.add_strdim("dict", list(2**x for x in range(2, 17)))
#     s.add_strdim("dict", [65536])  # [4096, 8192, 16384, 32768, 65536])
#     s.add_strdim("lc", [0, 1, 2, 3, 4])
#     s.add_strdim("lc", [4])
#     s.add_strdim("lp", [0, 1, 2, 3, 4])
#     s.add_strdim("lp", [0])
#     s.add_strdim("pb", [0, 1, 2, 3, 4])
#     s.add_strdim("mode", ["fast", "normal"])
#     s.add_strdim("mode", ["normal"])
#     s.add_strdim("nice", [4, 270])
#     s.add_strdim("nice", list(range(4, 270)))
#     s.add_strdim("mf", ["hc3", "hc4", "bt2", "bt3", "bt4"])
#     s.add_strdim("mf", ["bt4"])
#     s.add_strdim("depth", [1, 0, 1000])
#     s.add_strdim("depth", list(range(1, 1000)))
#     s.add_strdim("depth", [74])
#     # for v in s.cube_gen():
#     #    yield "--lzma1=" + ",".join(sorted(v))
#     for v in s.gen():
#         yield "--lzma1=" + ",".join(sorted(v))
#
#
# def redraw(datapoints):
#     x = []
#     y = []
#     for p in datapoints.keys():
#         if int(datapoints[p][1]) != 0:
#             x.append(int(datapoints[p][1]))
#             y.append(float(datapoints[p][0]))
#     plt.scatter(x, y, color='red', marker='.', s=0.5)
#     plt.grid(b=True, which='both', axis='both',
#              color='b', linestyle=':', linewidth=0.5)
#     plt.xscale("linear")
#     plt.xlabel("size, b")
#     plt.yscale("linear")
#     plt.ylabel("time, s")
#     plt.autoscale(enable=True)
#     plt.savefig("z_%s.png" % int(time.time()), dpi=200)
#
#
# if __name__ == '__main__': # noqa: MC0001
#     known_datapoints = {}
#     for fname in ["d:/my/src/xzperf/xzperf.txt",
#                   "d:/my/src/xzperf/xzperf_err.txt"]:
#         if not os.path.exists(fname):
#             continue
#         with open(fname, "r") as f:
#             for x in f.read().splitlines():
#                 dp = x.split("\t")
#                 if dp[2] in known_datapoints:
#                     print("duplicate: %s" % dp)
#                     sys.exit(0)
#                     if known_datapoints[dp[2]][0] > dp[0]:
#                         known_datapoints[dp[2]] = [dp[0], dp[1]]
#                     continue
#                 known_datapoints[dp[2]] = [dp[0], dp[1]]
#     print("%d known datapoints" % len(known_datapoints))
#     POOL_SIZE = 6
#     pool = Pool(POOL_SIZE)
#     gen = chaingen()
#     last_draw_t = 0
#     while True:
#         t = time.time()
#         if t - last_draw_t > 1:
#             redraw(known_datapoints)
#             last_draw_t = t
#         tasks = []
#         for t in range(POOL_SIZE):
#             try:
#                 task = next(gen)
#             except StopIteration:
#                 if tasks:
#                     break
#                 redraw(known_datapoints)
#                 raise
#             while task in known_datapoints:
#                 print("skipping %s : %s" % (task, known_datapoints[task]))
#                 task = next(gen)
#             tasks.append(task)
#             known_datapoints[task] = [0, 0]
#         r = pool.map(invoke_xz, tasks)
#         for i in r:
#             known_datapoints[i[2]] = [i[0], i[1]]
#             fname = "d:/my/src/xzperf/xzperf.txt"
#             if i[1] == 0:
#                 fname = "d:/my/src/xzperf/xzperf_err.txt"
#             with open(fname, "a") as f:
#                 s = "%.2f\t%s\t%s\t%s" % (i[0], i[1], i[2], i[3].strip())
#                 f.write(s+"\n")
#                 print(s)
