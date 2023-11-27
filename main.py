from moviepy.editor import VideoFileClip, concatenate_videoclips

#OS MINUTOS DO VIDEO SÃO CONTATOS COMO SEGUNDOS (1015 SEGUNDOS = 16:55 MIN)
clipe1 = VideoFileClip('').subclip(0, 0)
clipe2 = VideoFileClip('').subclip(0, 0)
#EM SUBCLIP SÃO COLOCADOS OS SEGUNDOS INICIAIS E OS SEGUNDOS FINAIS A SEREM CORTADOS
#O VIDEO A SER CORTADO PRECISA ESTAR NA PASTA DE ORIGEM DO ARQUIVO MAIN.PY

video_concatenado = concatenate_videoclips([clipe1, clipe2])
video_concatenado.write_videofile('VideoEditado.mp4')
