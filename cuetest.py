import pygame
import sys
import codecs

pygame.init()
pygame.display.set_mode()
pygame.mixer.init()

pgmm = pygame.mixer.music

fn = sys.argv[1]
times_fn = sys.argv[2]

times_f = codecs.open(times_fn, encoding="ascii", errors='replace')#, encoding='utf-8')
cue_times = list(map(float, times_f.readlines()))
times_f.close()


pgmm.load(fn)
pygame.mixer.fadeout(500)

print("loaded file")

is_playing = False

started = False

cur_cue_idx = 0

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
#            print("got event here")
            if event.key == pygame.K_RETURN:
                print("got event")
                if not started:
                    started = True
                    pgmm.play()
                    is_playing = True
                    print("playing... maybe...")
                    continue
                    
                if is_playing:
                    #pgmm.pause()
                    print("fading out, maybe")
                    pgmm.fadeout(2000)
                    is_playing = False
                    continue
                    
                pgmm.play(start=cue_times[cur_cue_idx])
#                pgmm.set_pos(cue_times[cur_cue_idx])
                cur_cue_idx += 1
#                pgmm.unpause()
                is_playing = True
            if event.key == pygame.K_ESCAPE:
                break
