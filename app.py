import gradio as gr
import cv2
import numpy as np
from generate_512 import predit, parse_args


def gen_image(mask, prompt):
    args = parse_args()
    args.mask = mask
    args.input_text = prompt
    predit(args)
    return f'{str(0).zfill(6)}_mixed.png'

with gr.Blocks() as demo:
  with gr.Row():
    with gr.Column():
      gr.Markdown('Mask')
      image = gr.Image(type="numpy", label="请输入图片")
      gr.Examples([
              '27007.png',
              '29980.png'
        ], image)
    with gr.Column():
      gr.Markdown('Prompt')
      text = gr.Text(label='请输入文本', lines=5)
      gr.Examples(
          ['This man has beard of medium length. He is in his thirties.',
           'This woman is in her forties.'
           ],
          text)

  button = gr.Button('Generate', variant='primary')
  out_image = gr.Image(type='filepath')

  button.click(gen_image, [image, text], out_image)

gr.close_all()
demo.queue()
demo.launch()