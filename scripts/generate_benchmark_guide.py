import sys
import os
from collections import Counter

# Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rag.benchmark import load_benchmark_questions

def generate_guide():
    df = load_benchmark_questions()
    
    source_names = {
        'GHR': 'Genetics Home Reference (GHR)',
        'GARD': 'Genetic and Rare Diseases Information Center (GARD)',
        'NIDDK': 'National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK)',
        'NINDS': 'National Institute of Neurological Disorders and Stroke (NINDS)',
        'MPlusHealthTopics': 'MedlinePlus Health Topics (MPlus)',
        'NIHSeniorHealth': 'NIH Senior Health',
        'CDC': 'Centers for Disease Control and Prevention (CDC)',
        'CancerGov': 'National Cancer Institute (Cancer.gov)'
    }

    items = []
    domain_counts = Counter()

    for idx, row in df.iterrows():
        qid = row['question_id']
        qtext = str(row['question']).strip()
        focus = str(row['category']).strip()
        source = str(row.get('source', 'N/A')).strip()
        gold_ans = str(row['gold_answer']).strip()
        
        domain_counts[focus] += 1
        items.append({
            'index': idx + 1,
            'qid': qid,
            'focus': focus,
            'source': source,
            'source_full': source_names.get(source, source),
            'question': qtext,
            'gold_answer': gold_ans
        })

    md_path = 'data/benchmark_50_questions.md'
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('# Medical RAG 50-Question Benchmark Dataset Study Guide\n\n')
        f.write('This document contains the curated set of **50 clinical evaluation questions** randomly sampled exclusively from the **Top 3 Focus Areas** (`Breast Cancer`, `Prostate Cancer`, `Stroke`) in `gold_data.csv`.\n\n')
        
        f.write('## 1. Focus Area Distribution Overview\n\n')
        f.write('| Focus Area | Question Count | Percentage |\n')
        f.write('|---|---|---|\n')
        for dom, count in domain_counts.most_common():
            pct = (count / len(items)) * 100
            f.write(f'| **{dom}** | {count} | {pct:.1f}% |\n')
        f.write('\n---\n\n')

        f.write('## 2. Quick Reference Table\n\n')
        f.write('| # | QID | Focus Area | Source | Question |\n')
        f.write('|---|---|---|---|---|\n')
        for it in items:
            f.write(f"| {it['index']:02d} | `{it['qid']}` | {it['focus']} | {it['source']} | {it['question']} |\n")
        
        f.write('\n---\n\n')
        f.write('## 3. Detailed Question & Gold Answer Reference\n\n')
        for it in items:
            f.write(f"### {it['index']:02d}. [{it['qid']}] {it['focus']}\n")
            f.write(f"- **Focus Area**: {it['focus']}\n")
            f.write(f"- **Data Source**: {it['source_full']}\n")
            f.write(f"- **Question**: {it['question']}\n\n")
            f.write(f"**Gold Standard Reference Answer**:\n> {it['gold_answer']}\n\n")
            f.write('---\n\n')

    print(f'Successfully regenerated {md_path} with {len(items)} complete entries.')

if __name__ == '__main__':
    generate_guide()
