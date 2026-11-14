# The 14 models and the 14 dictionaries. Sourced by the other scripts.
MODELS="meta-llama/Llama-3.2-1B meta-llama/Llama-3.2-1B-Instruct google/gemma-2b google/gemma-2b-it meta-llama/Llama-3.2-3B meta-llama/Llama-3.2-3B-Instruct Qwen/Qwen2.5-3B Qwen/Qwen2.5-3B-Instruct Qwen/Qwen2.5-7B Qwen/Qwen2.5-7B-Instruct meta-llama/Llama-3.1-8B meta-llama/Llama-3.1-8B-Instruct Qwen/Qwen2.5-14B Qwen/Qwen2.5-14B-Instruct"
# the eight models up to 3B parameters (Jacobian lens; heads on the follow-up pairs)
SMALL_MODELS="meta-llama/Llama-3.2-1B meta-llama/Llama-3.2-1B-Instruct google/gemma-2b google/gemma-2b-it meta-llama/Llama-3.2-3B meta-llama/Llama-3.2-3B-Instruct Qwen/Qwen2.5-3B Qwen/Qwen2.5-3B-Instruct"
DEVICE="${DEVICE:-mps}"
# dictionary tag | model | layer | site   (weights in dictionaries/<tag>/; the Llama-3.1-8B dictionary is Llama Scope, see README)
DICTIONARIES="llama-3.2-1B-base|meta-llama/Llama-3.2-1B|7|resid_post
llama-3.2-1B-base-k128|meta-llama/Llama-3.2-1B|7|resid_post
llama-3.2-1B-IT|meta-llama/Llama-3.2-1B-Instruct|7|resid_post
llama-3.2-1B-IT-k128|meta-llama/Llama-3.2-1B-Instruct|7|resid_post
llama-3.2-1B-base-MLP0|meta-llama/Llama-3.2-1B|0|mlp_out
llama-3.2-3B-base|meta-llama/Llama-3.2-3B|11|resid_post
llama-3.2-3B-base-k128|meta-llama/Llama-3.2-3B|11|resid_post
llama-3.2-3B-IT-k128|meta-llama/Llama-3.2-3B-Instruct|11|resid_post
llama-3.2-3B-IT-L3|meta-llama/Llama-3.2-3B-Instruct|3|resid_post
llama-3.2-3B-IT-L7|meta-llama/Llama-3.2-3B-Instruct|7|resid_post
llama-3.2-3B-IT-L19|meta-llama/Llama-3.2-3B-Instruct|19|resid_post
llama-3.1-8B-base|meta-llama/Llama-3.1-8B|12|resid_post
qwen-2.5-7b-base|Qwen/Qwen2.5-7B|0|resid_post
qwen-2.5-7b-IT|Qwen/Qwen2.5-7B-Instruct|0|resid_post"
dict_source() {   # --sae-dir or --llama-scope argument of a dictionary
  if [ "$1" = "llama-3.1-8B-base" ]; then echo "--llama-scope dictionaries/Llama3_1-8B-Base-L12R-8x"; else echo "--sae-dir dictionaries/$1"; fi
}
