#!/usr/bin/env python

print("# groupby-pydatatable.py", flush=True)

import os
import gc
import timeit
import datatable as dt
from datatable import f, sum, mean, count, sd, min, max, by, sort

exec(open("./helpers.py").read())

ver = dt.__version__
git = dt.__git_revision__
task = "groupby"
solution = "pydatatable"
fun = "[.datatable"
cache = "TRUE"

data_name = os.environ['SRC_GRP_LOCAL']
src_grp = os.path.join("data", data_name+".csv")
print("loading dataset %s" % data_name, flush=True)

x = dt.fread(src_grp)
print(x.nrows, flush=True)

print("grouping...", flush=True)

question = "sum v1 by id1" # q1
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"v1": sum(f.v1)}, by(f.id1)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, sum(f.v1)]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"v1": sum(f.v1)}, by(f.id1)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, sum(f.v1)]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans

question = "sum v1 by id1:id2" # q2
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"v1": sum(f.v1)}, by(f.id1, f.id2)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, sum(f.v1)]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"v1": sum(f.v1)}, by(f.id1, f.id2)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, sum(f.v1)]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans

question = "sum v1 mean v3 by id3" # q3
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"v1": sum(f.v1), "v3": mean(f.v3)}, by(f.id3)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v3)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"v1": sum(f.v1), "v3": mean(f.v3)}, by(f.id3)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v3)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans

question = "mean v1:v3 by id4" # q4
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"v1": mean(f.v1), "v2": mean(f.v2), "v3": mean(f.v3)}, by(f.id4)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2), sum(f.v3)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"v1": mean(f.v1), "v2": mean(f.v2), "v3": mean(f.v3)}, by(f.id4)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2), sum(f.v3)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans

question = "sum v1:v3 by id6" # q5
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"v1": sum(f.v1), "v2": sum(f.v2), "v3": sum(f.v3)}, by(f.id6)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2), sum(f.v3)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"v1": sum(f.v1), "v2": sum(f.v2), "v3": sum(f.v3)}, by(f.id6)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2), sum(f.v3)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans

#question = "median v3 sd v3 by id2 id4" # q6 # median not yet implemented https://github.com/h2oai/datatable/issues/1530
#gc.collect()
#t_start = timeit.default_timer()
#ans = x[:, {"median_v3": median(f.v3), "sd_v3": sd(f.v3)}, by(f.id2, f.id4)]
#print(ans.shape, flush=True)
#t = timeit.default_timer() - t_start
#m = memory_usage()
#t_start = timeit.default_timer()
#chk = ans[:, [sum(f.median_v3), sum(f.sd_v3)]]
#chkt = timeit.default_timer() - t_start
#write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
#del ans
#gc.collect()
#t_start = timeit.default_timer()
#ans = x[:, {"median_v3": median(f.v3), "sd_v3": sd(f.v3)}, by(f.id2, f.id4)]
#print(ans.shape, flush=True)
#t = timeit.default_timer() - t_start
#m = memory_usage()
#t_start = timeit.default_timer()
#chk = ans[:, [sum(f.median_v3), sum(f.sd_v3)]]
#chkt = timeit.default_timer() - t_start
#write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
#print(ans.head(3).to_pandas(), flush=True)
#print(ans.tail(3).to_pandas(), flush=True)
#del ans

question = "max v1 - min v2 by id2 id4" # q7
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"range_v1_v2": max(f.v1)-min(f.v2)}, by(f.id2, f.id4)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, sum(f.range_v1_v2)]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"range_v1_v2": max(f.v1)-min(f.v2)}, by(f.id2, f.id4)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, sum(f.range_v1_v2)]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans

question = "largest two v3 by id2 id4" # q8
gc.collect()
t_start = timeit.default_timer()
ans = x[:2, {"largest2_v3": f.v3}, by(f.id2, f.id4), sort(-f.v3)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, sum(f.largest2_v3)]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans
gc.collect()
t_start = timeit.default_timer()
ans = x[:2, {"largest2_v3": f.v3}, by(f.id2, f.id4), sort(-f.v3)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, sum(f.largest2_v3)]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans

#question = "regression v1 v2 by id2 id4" # q9 # cor or cov+var not yet implemeneted https://github.com/h2oai/datatable/issues/290#issuecomment-453075433
#gc.collect()
#t_start = timeit.default_timer()
#ans = x[:, {"r2": cor(v1, v2)^2}, by(f.id2, f.id4)]
#print(ans.shape, flush=True)
#t = timeit.default_timer() - t_start
#m = memory_usage()
#t_start = timeit.default_timer()
#chk = ans[:, sum(f.r2)]
#chkt = timeit.default_timer() - t_start
#write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
#del ans
#gc.collect()
#t_start = timeit.default_timer()
#ans = x[:, {"r2": cor(v1, v2)^2}, by(f.id2, f.id4)]
#print(ans.shape, flush=True)
#t = timeit.default_timer() - t_start
#m = memory_usage()
#t_start = timeit.default_timer()
#chk = ans[:, sum(f.r2)]
#chkt = timeit.default_timer() - t_start
#write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
#print(ans.head(3).to_pandas(), flush=True)
#print(ans.tail(3).to_pandas(), flush=True)
#del ans

question = "sum v3 count by id1:id6" # q10
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"v3": sum(f.v3), "count": count()}, by(f.id1, f.id2, f.id3, f.id4, f.id5, f.id6)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v3), sum(f.count)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans
gc.collect()
t_start = timeit.default_timer()
ans = x[:, {"v3": sum(f.v3), "count": count()}, by(f.id1, f.id2, f.id3, f.id4, f.id5, f.id6)]
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v3), sum(f.count)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans

exit(0)
