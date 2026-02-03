import sys

test_count = int(sys.stdin.readline())
seminar_dict = {
    "Algorithm" : "204",
    "DataAnalysis" : "207",
    "ArtificialIntelligence" : "302",
    "CyberSecurity" : "B101",
    "Network" : "303",
    "Startup" : "501",
    "TestStrategy" : "105",
}
for _ in range(test_count):
    seminar = sys.stdin.readline().strip()
    print(seminar_dict[seminar])
