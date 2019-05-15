def main():
    scores = {'Yang': 95, 'Lin': 78, 'Huang': 82}
    print(scores['Yang'])
    print(scores['Lin'])
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    scores['Kao'] = 65
    scores['Wang'] = 71
    scores.update(chang=67, tang=85)
    print(scores)
    if 'Kao' in scores:
        print(scores['Kao'])
    print(scores.get('Kao'))
    print(scores.get('ao', 60))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('Lin', 78))
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()