### A Pluto.jl notebook ###
# v0.18.0

using Markdown
using InteractiveUtils

# ╔═╡ 2b9ceb50-a2ad-4698-b30d-de9b8f7f697c
# Steps:
# 1. read data (X_train, y_train), (X_test, y_test). shape(X): N x D, shape(y): N x 1
# 2. compute objective function J(θ), shape(θ) = K x D
# 3. training: find θ_best, J(θ_best) minimizes J(θ) using Optim
# 4. evaluation: compute training accuracy, test accuracy

# ╔═╡ 36facda0-bfa8-11ec-1e75-1f3477c20ca8
using DelimitedFiles
using Optim

# ╔═╡ 71e62768-f6ba-4dfb-a8aa-164fec63c283
function readData()
	path = 
end

# ╔═╡ Cell order:
# ╠═2b9ceb50-a2ad-4698-b30d-de9b8f7f697c
# ╠═36facda0-bfa8-11ec-1e75-1f3477c20ca8
# ╠═71e62768-f6ba-4dfb-a8aa-164fec63c283
