#!/usr/bin/env julia

print("# groupby-juliadf.jl\n"); flush(stdout);

using DataFrames;
using CSV;
using Statistics; # mean function

include("$(pwd())/helpers.jl");

pkgmeta = getpkgmeta("DataFrames");
ver = pkgmeta["version"];
git = pkgmeta["git-tree-sha1"];
task = "groupby";
solution = "juliadf";
fun = "by";
cache = true;

data_name = ENV["SRC_GRP_LOCAL"];
src_grp = string("data/", data_name, ".csv")
println(string("loading dataset ", data_name)); flush(stdout);

x = CSV.read(src_grp, categorical=0.05, allowmissing=:none);
in_rows = size(x, 1);
println(in_rows); flush(stdout);

print("grouping...\n"); flush(stdout);

question = "sum v1 by id1"; # q1
GC.gc();
t = @elapsed (ANS = by(x, :id1, v1 = :v1 => sum); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = sum(ANS.v1);
write_log(1, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
ANS = 0;
GC.gc();
t = @elapsed (ANS = by(x, :id1, v1 = :v1 => sum); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = sum(ANS.v1);
write_log(2, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
println(first(ANS, 3));
println(last(ANS, 3));
ANS = 0;

question = "sum v1 by id1:id2"; # q2
GC.gc();
t = @elapsed (ANS = by(x, [:id1, :id2], v1 = :v1 => sum); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = sum(ANS.v1);
write_log(1, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
ANS = 0;
GC.gc();
t = @elapsed (ANS = by(x, [:id1, :id2], v1 = :v1 => sum); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = sum(ANS.v1);
write_log(2, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
println(first(ANS, 3));
println(last(ANS, 3));
ANS = 0;

question = "sum v1 mean v3 by id3"; # q3
GC.gc();
t = @elapsed (ANS = by(x, :id3, v1 = :v1 => sum, v3 = :v3 => mean); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = [sum(ANS.v1), sum(ANS.v3)];
write_log(1, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
ANS = 0;
GC.gc();
t = @elapsed (ANS = by(x, :id3, v1 = :v1 => sum, v3 = :v3 => mean); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = [sum(ANS.v1), sum(ANS.v3)];
write_log(2, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
println(first(ANS, 3));
println(last(ANS, 3));
ANS = 0;

question = "mean v1:v3 by id4"; # q4
GC.gc();
t = @elapsed (ANS = by(x, :id4, v1 = :v1 => mean, v2 = :v2 => mean, v3 = :v3 => mean); println(size(ANS)); flush(stdout));
m = memory_usage();
t_start = time_ns();
chkt = @elapsed chk = [sum(ANS.v1), sum(ANS.v2), sum(ANS.v3)];
write_log(1, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
ANS = 0;
GC.gc();
t = @elapsed (ANS = by(x, :id4, v1 = :v1=>mean, v2 = :v2=>mean, v3 = :v3=>mean); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = [sum(ANS.v1), sum(ANS.v2), sum(ANS.v3)];
write_log(2, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
println(first(ANS, 3));
println(last(ANS, 3));
ANS = 0;

question = "sum v1:v3 by id6"; # q5
GC.gc();
t = @elapsed (ANS = by(x, :id6, v1 = :v1 => sum, v2 = :v2 => sum, v3 = :v3 => sum); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = [sum(ANS.v1), sum(ANS.v2), sum(ANS.v3)];
write_log(1, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
ANS = 0;
GC.gc();
t = @elapsed (ANS = by(x, :id6, v1 = :v1 => sum, v2 = :v2 => sum, v3 = :v3 => sum); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = [sum(ANS.v1), sum(ANS.v2), sum(ANS.v3)];
write_log(2, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
println(first(ANS, 3));
println(last(ANS, 3));
ANS = 0;

question = "median v3 sd v3 by id2 id4"; # q6
GC.gc();
t = @elapsed (ANS = by(x, [:id2, :id4], median_v3 = :v3 => median, sd_v3 = :v3 => std); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = [sum(ANS.median_v3), sum(ANS.sd_v3)];
write_log(1, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
ANS = 0;
GC.gc();
t = @elapsed (ANS = by(x, [:id2, :id4], median_v3 = :v3 => median, sd_v3 = :v3 => std); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = [sum(ANS.median_v3), sum(ANS.sd_v3)];;
write_log(2, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
println(first(ANS, 3));
println(last(ANS, 3));
ANS = 0;

question = "max v1 - min v2 by id2 id4"; # q7
GC.gc();
t = @elapsed (ANS = by(x, [:id2, :id4], range_v1_v2 = [:v1, :v2] => x -> maximum(skipmissing(x.v1))-minimum(skipmissing(x.v2))); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = sum(ANS.range_v1_v2);
write_log(1, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
ANS = 0;
GC.gc();
t = @elapsed (ANS = by(x, [:id2, :id4], range_v1_v2 = [:v1, :v2] => x -> maximum(skipmissing(x.v1))-minimum(skipmissing(x.v2))); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = sum(ANS.range_v1_v2);
write_log(2, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
println(first(ANS, 3));
println(last(ANS, 3));
ANS = 0;

question = "largest two v3 by id2 id4"; # q8
GC.gc();
t = @elapsed (ANS = by(x, [:id2, :id4], largest2_v3 = :v3 => x -> partialsort(x, 1:2, rev=true)); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = sum(ANS.largest2_v3);
write_log(1, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
ANS = 0;
GC.gc();
t = @elapsed (ANS = by(x, [:id2, :id4], largest2_v3 = :v3 => x -> partialsort(x, 1:2, rev=true)); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = sum(ANS.largest2_v3);
write_log(2, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
println(first(ANS, 3));
println(last(ANS, 3));
ANS = 0;

question = "regression v1 v2 by id2 id4"; # q9
GC.gc();
t = @elapsed (ANS = by(x, [:id2, :id4], r2 = [:v1, :v2] => x -> cor(x.v1, x.v2)^2); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = sum(ANS.r2);
write_log(1, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
ANS = 0;
GC.gc();
t = @elapsed (ANS = by(x, [:id2, :id4], r2 = [:v1, :v2] => x -> cor(x.v1, x.v2)^2); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = sum(ANS.r2);
write_log(2, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
println(first(ANS, 3));
println(last(ANS, 3));
ANS = 0;

question = "sum v3 count by id1:id6"; # q10
GC.gc();
t = @elapsed (ANS = by(x, [:id1, :id2, :id3, :id4, :id5, :id6], v3 = :v3 => sum, count = :v3 => length); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = [sum(ANS.v3), sum(ANS.count)];
write_log(1, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
ANS = 0;
GC.gc();
t = @elapsed (ANS = by(x, [:id1, :id2, :id3, :id4, :id5, :id6], v3 = :v3 => sum, count = :v3 => length); println(size(ANS)); flush(stdout));
m = memory_usage();
chkt = @elapsed chk = [sum(ANS.v3), sum(ANS.count)];
write_log(2, task, data_name, in_rows, question, size(ANS, 1), size(ANS, 2), solution, ver, git, fun, t, m, cache, make_chk(chk), chkt);
println(first(ANS, 3));
println(last(ANS, 3));
ANS = 0;

exit();
