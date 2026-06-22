#!/usr/bin/env python3
"""EC2 rightsizing recommendations."""
import boto3

def get_rightsizing_recommendations():
    client = boto3.client('compute-optimizer')
    response = client.get_ec2_instance_recommendations()
    
    for rec in response['instanceRecommendations']:
        current = rec['currentInstanceType']
        recommended = rec['recommendationOptions'][0]['instanceType']
        savings = rec['recommendationOptions'][0]['savingsOpportunity']['estimatedMonthlySavings']
        print(f"{rec['instanceArn'].split('/')[-1]}: {current} -> {recommended} (save ${savings['amount']}/mo)")
        
    return response['instanceRecommendations']
