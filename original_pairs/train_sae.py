"""Trains one TopK sparse autoencoder with SAELens (version 6.43): 500 million tokens of SlimPajama, eight times as many features as the hidden state has dimensions."""
import argparse
from sae_lens import LanguageModelSAERunnerConfig, SAETrainingRunner, LoggingConfig
from sae_lens.saes import TopKTrainingSAEConfig

ap = argparse.ArgumentParser()
ap.add_argument("--model", required=True, help="e.g. meta-llama/Llama-3.2-1B"); ap.add_argument("--hook", required=True, help="e.g. blocks.7.hook_resid_post or blocks.0.hook_mlp_out")
ap.add_argument("--d-in", type=int, required=True); ap.add_argument("--k", type=int, default=64); ap.add_argument("--tokens", type=int, default=500_000_000)
ap.add_argument("--dataset", default="DKYoon/SlimPajama-6B"); ap.add_argument("--device", default="cuda"); ap.add_argument("--out", required=True); ap.add_argument("--seed", type=int, default=42)
a = ap.parse_args()
sae = TopKTrainingSAEConfig(d_in=a.d_in, d_sae=8 * a.d_in, k=a.k, aux_loss_coefficient=1 / 32, device=a.device, decoder_init_norm=0.1, apply_b_dec_to_input=True,
                            normalize_activations="none", rescale_acts_by_decoder_norm=True, use_sparse_activations=False, dtype="float32")
cfg = LanguageModelSAERunnerConfig(sae=sae, model_name=a.model, hook_name=a.hook, dataset_path=a.dataset, is_dataset_tokenized=False, streaming=True, context_size=512, seqpos_slice=(4, None),
                                   training_tokens=a.tokens, train_batch_size_tokens=4096, lr=1e-4, adam_beta1=0.9, adam_beta2=0.999, lr_scheduler_name="constant", lr_warm_up_steps=5000,
                                   lr_decay_steps=0, dead_feature_window=1000, feature_sampling_window=2000, dead_feature_threshold=1e-6, device=a.device, seed=a.seed, dtype="float32",
                                   prepend_bos=True, compile_llm=False, compile_sae=False, autocast=False, autocast_lm=False, checkpoint_path=a.out, save_final_checkpoint=True,
                                   n_checkpoints=10, logger=LoggingConfig(log_to_wandb=False, log_activations_store_to_wandb=False, log_optimizer_state_to_wandb=False, log_weights_to_wandb=False))
SAETrainingRunner(cfg).run()
