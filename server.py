import gradio as gr
from generate_512 import predict, parse_args
from functools import partial


def gen_image(image_path, text):
    args = parse_args()
    args.mask_path = image_path[0]
    args.input_text = text
    print(args.mask_path)
    save_mixed_path = predict(args)
    return save_mixed_path


if __name__ == "__main__":
    title = """<h1 align="center">Collaborative Diffusion (CVPR 2023)</h1>"""

    theme = gr.themes.Soft(
        primary_hue="zinc",
        secondary_hue="green",
        neutral_hue="green",
        text_size=gr.themes.sizes.text_lg)

    with gr.Blocks(
            css=
            """#col_container { margin-left: auto; margin-right: auto;}""",
            theme=theme) as demo:
        gr.HTML(title)
        with gr.Row(elem_id="col_container"):
            with gr.Column():
                gr.Markdown('Mask')
                # in_image = gr.Image(
                #     type="filepath", label="请输入图片", source="upload")
                # gr.Examples([
                #     'test_data/512_masks/27007.png',
                #     'test_data/512_masks/29980.png'
                # ],
                #             inputs=in_image)
                examples = gr.Dataset(
                    label="请选择 Mask",
                    components=[gr.Image(visible=False)],
                    samples=[['test_data/512_masks/27007.png'],
                             ['test_data/512_masks/29980.png']])
                button = gr.Button('Generate', variant='primary')
                out_image = gr.Image(type='filepath')
            with gr.Column():
                gr.Markdown('Prompt')
                text = gr.Text(label='请输入文本', lines=5)
                gr.Examples([
                    'This man has beard of medium length. He is in his thirties.',
                    'This woman is in her forties.'
                ],
                            inputs=text)

        button.click(partial(gen_image), [examples, text], out_image)

    gr.close_all()
    demo.launch(share=True, debug=True)