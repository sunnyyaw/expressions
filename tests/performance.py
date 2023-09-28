import cProfile
import main
import pstats
import io
pr = cProfile.Profile()
pr.enable()
main.main()
pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr,stream=s).sort_stats('tottime')
ps.print_stats()
with open('performance.txt','w+')as f:
    f.write(s.getvalue())
