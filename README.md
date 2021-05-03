# coherence_denoising
Introduce noise to disrupt coherence, and experiment with models attempting to remove this noise.


Game plan:
1) Enable chunking of wikihow dataset.
2) Split wikihow into test/train/validation datasets.
3) Split a wiki-entry into >= 1 `Parts`. 
   Each part consists of an ordered sequence of steps. 
   We want to record the original order of these steps, and then shuffle these steps. 