### A Pluto.jl notebook ###
# v0.18.0

using Markdown
using InteractiveUtils

# ╔═╡ dc929ce0-c29e-11ec-3c7d-8d4a5494331f
begin
	using DelimitedFiles
	using Statistics
end

# ╔═╡ 70964863-7c4f-4814-831b-3eb1974c36d6
function readData(path)
	# for breast cancer dataset
	A = readdlm(path, ',')
	X = A[:,3:end]
	y = Int.(A[:,2]).+1
	return (X, y)
end

# ╔═╡ c046a9db-00b7-41ea-8179-5cb28e0ae6ac
function readData2(path)
	# for iris flower dataset
	A = readdlm(path, '\t')
	X = A[:,2:end]
	y = Int.(A[:,1])
	return (X, y)
end

# ╔═╡ e54e6155-8cc7-436c-a547-ae7bf3cae6ae
function train(X, y)
	N, D = size(X)
	K = length(unique(y))
	θ = zeros(K)
	μ = zeros(D,K)
	σ = zeros(D,K)
	for k=1:K
		idk = (y.==k)
		θ[k] = sum(idk)/N
		μ[:,k] = vec(mean(X[idk,:], dims=1))
		σ[:,k] = vec(std(X[idk,:], dims=1))
	end
	return (θ, μ, σ)
end

# ╔═╡ e056067f-d850-4b99-b2fb-359938838d17
function classify(xNew, θ, μ, σ)
	D, K = size(μ)
	scores = zeros(K)
	for k=1:K
		scores[k] = log(θ[k])
		for j=1:D
			scores[k] += log(1/sqrt(2*pi*σ[j,k])) - ((xNew[j]-μ[j,k])^2)/(2*σ[j,k])
		end
	end
	return argmax(scores)
end

# ╔═╡ e82d264f-84c0-4087-9d1e-8030092c8dad
function evaluate(X, y, θ, μ, σ)
	N = length(y)
	cl = map(i -> classify(X[i,:], θ, μ, σ), 1:N)
	return sum(cl .== y)/N
end

# ╔═╡ 87338395-eb6f-4471-9669-bd43ecc3f95e
begin
	# X, y = readData("../data/wdbc.txt")
	X, y = readData2("../data/iris-train.txt")
	X_test, y_test = readData2("../data/iris-test.txt")
end

# ╔═╡ 53bb9f3a-bce0-4162-beda-7567a1a305b3
θ, μ, σ = train(X, y)

# ╔═╡ a1672e8e-74ea-4762-aefa-c7afa542f7ad
ev = evaluate(X_test, y_test, θ, μ, σ)

# ╔═╡ 00000000-0000-0000-0000-000000000001
PLUTO_PROJECT_TOML_CONTENTS = """
[deps]
DelimitedFiles = "8bb1440f-4735-579b-a4ab-409b98df4dab"
Statistics = "10745b16-79ce-11e8-11f9-7d13ad32a3b2"
"""

# ╔═╡ 00000000-0000-0000-0000-000000000002
PLUTO_MANIFEST_TOML_CONTENTS = """
# This file is machine-generated - editing it directly is not advised

julia_version = "1.7.2"
manifest_format = "2.0"

[[deps.Artifacts]]
uuid = "56f22d72-fd6d-98f1-02f0-08ddc0907c33"

[[deps.CompilerSupportLibraries_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "e66e0078-7015-5450-92f7-15fbd957f2ae"

[[deps.DelimitedFiles]]
deps = ["Mmap"]
uuid = "8bb1440f-4735-579b-a4ab-409b98df4dab"

[[deps.Libdl]]
uuid = "8f399da3-3557-5675-b5ff-fb832c97cbdb"

[[deps.LinearAlgebra]]
deps = ["Libdl", "libblastrampoline_jll"]
uuid = "37e2e46d-f89d-539d-b4ee-838fcccc9c8e"

[[deps.Mmap]]
uuid = "a63ad114-7e13-5084-954f-fe012c677804"

[[deps.OpenBLAS_jll]]
deps = ["Artifacts", "CompilerSupportLibraries_jll", "Libdl"]
uuid = "4536629a-c528-5b80-bd46-f80d51c5b363"

[[deps.Random]]
deps = ["SHA", "Serialization"]
uuid = "9a3f8284-a2c9-5f02-9a11-845980a1fd5c"

[[deps.SHA]]
uuid = "ea8e919c-243c-51af-8825-aaa63cd721ce"

[[deps.Serialization]]
uuid = "9e88b42a-f829-5b0c-bbe9-9e923198166b"

[[deps.SparseArrays]]
deps = ["LinearAlgebra", "Random"]
uuid = "2f01184e-e22b-5df5-ae63-d93ebab69eaf"

[[deps.Statistics]]
deps = ["LinearAlgebra", "SparseArrays"]
uuid = "10745b16-79ce-11e8-11f9-7d13ad32a3b2"

[[deps.libblastrampoline_jll]]
deps = ["Artifacts", "Libdl", "OpenBLAS_jll"]
uuid = "8e850b90-86db-534c-a0d3-1478176c7d93"
"""

# ╔═╡ Cell order:
# ╠═dc929ce0-c29e-11ec-3c7d-8d4a5494331f
# ╠═70964863-7c4f-4814-831b-3eb1974c36d6
# ╠═c046a9db-00b7-41ea-8179-5cb28e0ae6ac
# ╠═e54e6155-8cc7-436c-a547-ae7bf3cae6ae
# ╠═e056067f-d850-4b99-b2fb-359938838d17
# ╠═e82d264f-84c0-4087-9d1e-8030092c8dad
# ╠═87338395-eb6f-4471-9669-bd43ecc3f95e
# ╠═53bb9f3a-bce0-4162-beda-7567a1a305b3
# ╠═a1672e8e-74ea-4762-aefa-c7afa542f7ad
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002
