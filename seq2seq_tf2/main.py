import argparse
from train_test_eval import train, test_and_save, evaluate
import os
import warnings

warnings.filterwarnings('ignore')

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--max_enc_len", default=800, help="Encoder input max sequence length", type=int)
  parser.add_argument("--max_dec_len", default=60, help="Decoder input max sequence length", type=int)
  parser.add_argument("--max_dec_steps", default=60, help="maximum number of words of the predicted report", type=int)
  parser.add_argument("--min_dec_steps", default=0, help="Minimum number of words of the predicted report", type=int)
  parser.add_argument("--batch_size", default=4, help="batch size", type=int)
  parser.add_argument("--beam_size", default=4, help="beam size for beam search decoding (must be equal to batch size in decode mode)", type=int)
  parser.add_argument("--vocab_size", default=50000, help="Vocabulary size", type=int)
  parser.add_argument("--embed_size", default=100, help="Words embeddings dimension", type=int)
  parser.add_argument("--enc_units", default=256, help="Encoder GRU cell units number", type=int)
  parser.add_argument("--dec_units", default=256, help="Decoder GRU cell units number", type=int)
  parser.add_argument("--attn_units", default=512, help="[context vector, decoder state, decoder input] feedforward result dimension - this result is used to compute the attention weights", type=int)
  parser.add_argument("--learning_rate", default=0.15, help="Learning rate", type=float)
  parser.add_argument("--adagrad_init_acc", default=0.1, help="Adagrad optimizer initial accumulator value. Please refer to the Adagrad optimizer API documentation on tensorflow site for more details.", type=float)
  parser.add_argument("--max_grad_norm",default=0.8, help="Gradient norm above which gradients must be clipped", type=float)
  parser.add_argument("--checkpoints_save_steps", default=1000, help="Save checkpoints every N steps", type=int)
  parser.add_argument("--max_steps", default=100000, help="Max number of iterations", type=int)
  parser.add_argument("--num_to_test", default=50, help="Number of examples to test", type=int)
  parser.add_argument("--max_num_to_eval", default=500, help="Max number of examples to evaluate", type=int)
  parser.add_argument("--mode", help="train, eval or test options", default="eval", type=str)
  parser.add_argument("--model_path", help="Path to a specific model", default='', type=str)
  parser.add_argument("--checkpoint_dir", help="Checkpoint directory", default=os.path.join(os.path.abspath('../'), 'data', 'checkpoint_dir'), type=str)
  parser.add_argument("--test_save_dir", help="Directory in which we store the decoding results", default=os.path.join(os.path.abspath('../'), 'data', 'test_save_dir'), type=str)
  parser.add_argument("--data_dir",  help="Data Folder", default=os.path.join(os.path.abspath('../'), 'data', 'eval.csv'), type=str)
  parser.add_argument("--vocab_path", help="Vocab path", default=os.path.join(os.path.abspath('../'), 'data', 'words_frequences.txt'), type=str)
  parser.add_argument("--log_file", help="File in which to redirect console outputs", default=os.path.join(os.path.abspath('../'), 'data', 'log.txt'), type=str)


  args = parser.parse_args()
  params = vars(args)
  print(params)

  assert params["mode"], "mode is required. train, test or eval option"
  assert params["mode"] in ["train", "test", "eval"], "The mode must be train , test or eval"
  assert os.path.exists(params["data_dir"]), "data_dir doesn't exist"
  assert os.path.isfile(params["vocab_path"]), "vocab_path doesn't exist"


  if params["mode"] == "train":
    train(params)
  elif params["mode"] == "test":
    test_and_save(params)
  elif params["mode"] == "eval":
    evaluate(params)
  
  
if __name__ =="__main__":
  main()