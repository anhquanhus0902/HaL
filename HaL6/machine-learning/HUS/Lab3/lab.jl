#!/usr/bin/env julia

using DelimitedFiles
using Plots

function readData(path)
    f = readdlm(path, ',')
    y = f[:,2]
    N = length(y)
    X = f[:,2]
    X = [ones(N) X]
    return (X, y)
end    

function train(X, y)
    return inv(X'*X)*X'*y
end

X, y = readData("../Lab2/wdbc.txt")
plot(X[:,2], y, st=:scatter, legend=false, xlabel="Temperature", ylabel="Pressure")
