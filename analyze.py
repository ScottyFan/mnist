import sys
import re
import matplotlib.pyplot as plt

def parse_log(filename):
    """Extract accuracy and loss from log file"""
    with open(filename, 'r') as f:
        content = f.read()
    
    acc_pattern = r'Test set:.*?\(([\d.]+)%\)'
    accuracies = [float(x) for x in re.findall(acc_pattern, content)]
    
    loss_pattern = r'Test set: Average loss: ([\d.]+)'
    losses = [float(x) for x in re.findall(loss_pattern, content)]
    
    config = filename.replace('.log', '').replace('exp', 'Exp ')
    
    return {
        'name': config,
        'accuracies': accuracies,
        'losses': losses
    }

def plot_results(experiments):
    """Create comparison plots"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    for exp in experiments:
        epochs = range(1, len(exp['accuracies']) + 1)
        ax1.plot(epochs, exp['accuracies'], marker='o', label=exp['name'])
    
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Test Accuracy (%)')
    ax1.set_title('Test Accuracy Comparison')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    for exp in experiments:
        epochs = range(1, len(exp['losses']) + 1)
        ax2.plot(epochs, exp['losses'], marker='s', label=exp['name'])
    
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Test Loss')
    ax2.set_title('Test Loss Comparison')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('results_comparison.png', dpi=300, bbox_inches='tight')
    print(f"✓ Saved: results_comparison.png")
    
    # Print summary
    print("\n" + "="*60)
    print("EXPERIMENT SUMMARY")
    print("="*60)
    for exp in experiments:
        if exp['accuracies']:
            print(f"\n{exp['name']}:")
            print(f"  Final Accuracy: {exp['accuracies'][-1]:.2f}%")
            print(f"  Final Loss: {exp['losses'][-1]:.4f}")
            print(f"  Epochs: {len(exp['accuracies'])}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze.py exp1.log exp2.log exp3.log ...")
        print("\nOr specify log files:")
        print("  python analyze.py exp*.log")
        sys.exit(1)
    
    experiments = []
    for log_file in sys.argv[1:]:
        try:
            exp = parse_log(log_file)
            experiments.append(exp)
            print(f"Parsed: {log_file}")
        except FileNotFoundError:
            print(f"Not found: {log_file}")
        except Exception as e:
            print(f"Error parsing {log_file}: {e}")
    
    if experiments:
        plot_results(experiments)
    else:
        print("Invalid!")

if __name__ == '__main__':
    main()
