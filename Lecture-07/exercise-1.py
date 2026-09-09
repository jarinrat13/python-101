survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"]
]

choices_sets = [set(p) for p in survey_results]
common_languages = set.intersection(*choices_sets)
print("Languages chosen by all participants:", common_languages)

only_chosen_by_one_participant = [lang for lang in set.union(*choices_sets)if sum(lang in p for p in survey_results) == 1]
print("Languages only chosen by one participant:", only_chosen_by_one_participant)

number_of_unique_languages = len(set.union(*choices_sets))
print("Number of unique languages:", number_of_unique_languages)

languages_chosen_by_exactly_two_participants = [lang for lang in set.union(*choices_sets) if sum(lang in p for p in survey_results) == 2]
print("Languages chosen by exactly two participants:", languages_chosen_by_exactly_two_participants)

sets_list = [set(choices) for choices in survey_results]
result = []

for i in range(len(sets_list)):
    for j in range(i + 1, len(sets_list)):
        if sets_list[i] == sets_list[j]:
            result.append([i + 1, j + 1])
print("Participants with the same set of languages:", result)
