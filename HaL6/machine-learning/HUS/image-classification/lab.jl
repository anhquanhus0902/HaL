#!/usr/bin/env julia

using DelimitedFiles
using Optim

print("done")

function readData()
    path = "./segmentation.data"
    X = readlm(path, ',')
    print(X)
end

readData()
